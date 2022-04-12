import Data.Char
import Data.List



printerError :: [Char] -> [Char]
printerError s | 1 == 1 = (show len_n_z) ++ "/" ++ (show lenS)
    where ss = sort [ toLower c | c <- s ]
          len_n_z = length( findIndices (`elem` ['n'..'z']) ss)
          lenS = length s
