class AlatTulis:
  def __init__(self, name, stock, unit_price):
    self.name = name
    self.stock = stock
    self.unit_price = unit_price
    self.total_price = self.stock * self.unit_price

  def set_stock(self, stock):
    self.stock = stock
    self.total_price = self.stock * self.unit_price

  def set_unit_price(self, unit_price):
    self.unit_price = unit_price
    self.total_price = self.stock * self.unit_price

  def get_name(self):
    return self.name

  def get_stock(self):
    return self.stock

  def get_unit_price(self):
    return self.unit_price

  def get_total_price(self):
    return self.total_price

  def all_price(self, amount):
    return amount * self.unit_price

pen = AlatTulis("Bolpoint", 30, 2000)
pencil = AlatTulis("Pensil", 30, 1000)
eraser = AlatTulis("Penghapus", 30, 500)

print("\nStok Alat Tulis       :")
print(f"{pen.get_name()} \t Stok : {pen.get_stock()} | Harga : Rp.{pen.get_unit_price()}")
print(f"{pencil.get_name()} \t\t Stok : {pencil.get_stock()} | Harga : Rp.{pencil.get_unit_price()}")
print(f"{eraser.get_name()} \t Stok : {eraser.get_stock()} | Harga : Rp.{eraser.get_unit_price()}")

purchase_pen = 10
purchase_pencil = 10
purchase_eraser = 10
pen.set_stock(pen.get_stock() - purchase_pen)
pencil.set_stock(pencil.get_stock() - purchase_pencil)
eraser.set_stock(eraser.get_stock() - purchase_eraser)

total_pen = pen.all_price(purchase_pen)
total_pencil = pencil.all_price(purchase_pencil)
total_eraser = eraser.all_price(purchase_eraser)

print("\nHasil Transaksi:")
print(f"Bolpoint \tx {purchase_pen} = Rp.{total_pen}")
print(f"Pensil \t\tx {purchase_pencil} = Rp.{total_pencil}")
print(f"Penghapus \tx {purchase_eraser} = Rp.{total_eraser}")

all_purchase = total_pen + total_pencil + total_eraser
print(f"Total Transaksi      = Rp.{all_purchase}")

print("\nStok Setelah Transaksi:")
print(f"{pen.get_name()} \t Stok : {pen.get_stock()}")
print(f"{pencil.get_name()} \t\t Stok : {pencil.get_stock()}")
print(f"{eraser.get_name()} \t Stok : {eraser.get_stock()}")