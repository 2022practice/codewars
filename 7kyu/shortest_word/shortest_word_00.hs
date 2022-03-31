module FindShortest (find_shortest) where

find_shortest :: String -> Integer
find_shortest s = toInteger (minimum [ length w | w <- words s])
