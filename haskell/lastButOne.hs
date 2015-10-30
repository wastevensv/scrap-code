lastButOne xs
        | length xs == 2 = head xs
        | otherwise = lastButOne(tail xs)

elementAt :: Int -> [a] -> a
elementAt 1 xs = head xs
elementAt n xs = elementAt (n-1) (tail xs)

main = print (lastButOne "abc")

