import matplotlib.pyplot as plt
import numpy as np
# Karla Saenz NC 0133

cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 7000, 9000, 12000, 18000]

plt.plot(cant_productos,)
plt.show()

# perzonalizar grafica
plt.plot(cant_productos,precio)
plt.show

import matplotlib.pyplot as plt
import numpy as np

# Karla Saenz NC 0133
cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 7000, 9000, 12000, 18000]

# Gráfica con personalización corregida
plt.plot(
    cant_productos, 
    precio, 
    color="green",       
    marker="o",         
    linestyle="--",     
    markersize=12
)


plt.title("Relación entre Cantidad de Productos y Precio")
plt.xlabel("Cantidad de Productos")
plt.ylabel("Precio")

plt.show()