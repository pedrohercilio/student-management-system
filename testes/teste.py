var = "3"

if var.isnumeric():
    print("é numerico")

elif var.isdigit():
    print("é digito")

else:
    print("não é porra nenhuma")

print(f"numeric: {var.isnumeric()}, digito: {var.isdigit()}")