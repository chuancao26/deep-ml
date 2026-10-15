def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	col = len(a[0])
	fil = len(a)
	if col != len(b):
		return -1
	
	result = []

	for i in range(0, fil):
		acum = 0
		for j in range(0, col):
			acum += a[i][j] * b[j]
		result.append(acum)
	return result
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.