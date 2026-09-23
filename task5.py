import time
 
sizes = [1000, 10000, 100000]
 
print(f"{'Розмір':>8}{'Пошук у списку, мс':>22}{'Пошук у множині, мс':>22}")
for n in sizes:
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1
 
    start = time.perf_counter()
    _ = target in data_list
    list_time = (time.perf_counter() - start) * 1000
 
    start = time.perf_counter()
    _ = target in data_set
    set_time = (time.perf_counter() - start) * 1000
 
    print(f"{n:>8}{list_time:>22.5f}{set_time:>22.5f}")
