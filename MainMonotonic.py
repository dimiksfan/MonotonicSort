from time import monotonic
import CreateMonotonic as m




start = monotonic()

lst = m.CreateLst()

finish = monotonic()


print(round(finish - start, 2))

