from __future__ import print_function
import re, string
import sys
from sys import argv
import re
import gzip
import xml.etree.ElementTree as ET
from multiprocessing import Pool, Queue, freeze_support

def worker(input, output, query):
    for filename in iter(input.get,'STOP'):
        result = search_transcript(filename, query)
        output.put(result)

def search_transcript(filename, query):
    with gzip.open(filename, 'rb') as f:
        file_content = f.read()

    root = ET.fromstring(file_content)

    alpha_pattern = re.compile('[\W_]+')

    transcript = []

    with open(filename+'.sent.txt', 'w') as f:
            match = False
            for sentence in filter(lambda child: child.tag == "s", root):
                block = ""
                for word in filter(lambda child: child.tag == "w", sentence):
                    word = alpha_pattern.sub('', word.text)
                    if word == query: match = True
                    if word:
                        block += word + ' '
                        transcript.append(word)
                f.write(block + '\n')

    with open(filename+'.txt', 'w') as f:
        f.write(' '.join(transcript))

    return (filename,len(transcript), match)

def make_transcript(filename):
    with gzip.open(filename, 'rb') as f:
        file_content = f.read()

    root = ET.fromstring(file_content)

    alpha_pattern = re.compile('[\W_]+')

    transcript = []

    with open(filename+'.txt', 'w') as f:
        sent_count = 0
        for sentence in filter(lambda child: child.tag == "s", root):
            block = ""
            for word in filter(lambda child: child.tag == "w", sentence):
                block += alpha_pattern.sub('', word.text) + " "
            sent_count += 1
            f.write(block+'\n')

    return (filename,sent_count)

if __name__ == "__main__":
    import os

    freeze_support()
    NUMBER_OF_PROCESSES = 35

    tasks = Queue()
    results = Queue()

    try:
        pool = Pool(NUMBER_OF_PROCESSES, initializer=worker, initargs=(tasks, results, argv[2]))

        for (dirpath, dirnames, filenames) in os.walk(argv[1]):
            for filename in filenames:
                if filename.endswith(".xml.gz"):
                    path = os.path.join(dirpath,filename)
                    tasks.put(path)

        for i in range(NUMBER_OF_PROCESSES):
            tasks.put('STOP')

        print("Waiting for results...")
        while not tasks.empty():
            while not results.empty():
                (filename, sent_count, match) = results.get()
                print(filename,sent_count, match)
                print("Remaining", tasks.qsize())
    except KeyboardInterrupt:
        pool.close()
        print("Finishing.")
        exit = False
        while not exit:
            for proc in pool._pool:
                if proc.is_alive():
                    print(proc)
                    proc.terminate()
                exit |= proc.is_alive()
    print("Done.")
