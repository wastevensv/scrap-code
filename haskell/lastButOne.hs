lastButOne xs = if head xs == last xs
                             then xs
                             else lastButOne(tail xs)

main = print (lastButOne "abc")