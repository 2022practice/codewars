def printer_error(s):
   return f"{len([letter for letter in s if letter in 'nñopqrstuvwxyz'])}/{len(s)}"
