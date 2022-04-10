module SquareDigit where
import Data.Char

squareDigit :: Int -> Int
squareDigit n | n < 0 = - squareDigit(-n)
              | otherwise = read (concat [ show ((read [d] ::Int)^2)  | d <- show n ]) :: Int

