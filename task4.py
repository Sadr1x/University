group_a = ["id1", "id2", "id3", "id2", "id4"]
group_b = ["id3", "id4", "id5", "id5", "id6"]
 
set_a = set(group_a)
set_b = set(group_b)
 
print("Унікальні в group_a:", set_a)
print("Унікальні в group_b:", set_b)
 
print("\nПеретин (спільні):", set_a & set_b)
print("Об'єднання:", set_a | set_b)
print("Симетрична різниця:", set_a ^ set_b)
 
small = {"id3", "id4"}
print("\nЧи", small, "є підмножиною set_a:", small <= set_a)
print("Чи", small, "є підмножиною set_b:", small <= set_b)
print("Чи", set_a, "є підмножиною set_b:", set_a <= set_b)
