1. 
D1: total_amount >= 1000000
D2: is_vip (nằm trong nhánh True của D1)
D3: is_vip (nằm trong nhánh False của D1)
2. V(G) = 3 + 1 = 4
3. 
Đường đi	D1 (total_amount >= 1000000)	D2/D3 (is_vip)	Kết quả
Path 1	True	True	return 0
Path 2	True	False	return 20000
Path 3	False	True	return 30000
Path 4	False	False	return 50000