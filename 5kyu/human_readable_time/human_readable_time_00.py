def make_readable(seconds):
      sec = seconds%60
      minutes = seconds//60
      hours = 0
      if minutes > 59:
          hours = minutes//60
          minutes = minutes%60
      return f'{hours:02d}:{minutes:02d}:{sec:02d}'
