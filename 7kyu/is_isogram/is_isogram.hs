import Data.Char
import Data.List

isIsogram :: String -> Bool --en realidad es bool, pero vamos a probar 1ero
isIsogram s | length (idxs_c) > 1 = False
            | length s == 0 = True
            | otherwise = isIsogram( (delete c sortedS) )
    where sortedS = sort [ toLower c | c <- s ]
          lenS = (length sortedS) - 1
          c = sortedS!! lenS
          idxs_c = findIndices (`elem` [c]) sortedS
