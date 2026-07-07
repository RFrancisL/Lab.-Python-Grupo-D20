[proyecto2.py](https://github.com/user-attachments/files/29764808/proyecto2.py)
def ejecutar_sistema():
    # Sectores
    sectores = {
        "1": {"nombre": "Campo VIP", "capacidad": 500, "precio": 250000, "vendidos": 0},
        "2": {"nombre": "Campo General", "capacidad": 5000, "precio": 150000, "vendidos": 0},
        "3": {"nombre": "Platea Preferencial", "capacidad": 1500, "precio": 180000, "vendidos": 0},
        "4": {"nombre": "Platea Baja", "capacidad": 2500, "precio": 130000, "vendidos": 0},
        "5": {"nombre": "Platea Alta", "capacidad": 3000, "precio": 100000, "vendidos": 0},
        "6": {"nombre": "Popular", "capacidad": 5000, "precio": 70000, "vendidos": 0}
    }

    descuentos_map = {
        "1": ("Anticipado", 0.35),
        "2": ("Preventa", 0.15),
        "3": ("Pack", 0.23),
        "4": ("Membresía", 0.13),
        "5": ("Discapacidad", 1.0),
        "6": ("Ninguno", 0.0)
    }

    total_recaudado = 0
    
    while True:
        print("\n--- SELECCIONE SECTOR (1-6) ---")
        for k, v in sectores.items():
            print(f"{k}. {v['nombre']} (Disp: {v['capacidad'] - v['vendidos']})")
        
        # .strip() elimina espacios accidentales
        opc_s = input("Opción: ").strip()
        
        if opc_s not in sectores:
            print("Opción no válida. Intente de nuevo.")
            continue
        
        if sectores[opc_s]["vendidos"] >= sectores[opc_s]["capacidad"]:
            print("¡Error! Sector lleno.")
            continue

        print("\n--- SELECCIONE DESCUENTO (1-6) ---")
        for k, v in descuentos_map.items():
            print(f"{k}. {v[0]}")
        
        opc_d = input("Opción: ").strip()
        tasa = descuentos_map.get(opc_d, ("Ninguno", 0.0))[1]
        
        precio_final = sectores[opc_s]["precio"] * (1 - tasa)
        sectores[opc_s]["vendidos"] += 1
        total_recaudado += precio_final
        
        print(f"Ticket vendido. Precio final: ${precio_final:,.0f}")
        
        # Validación estricta sin .lower()
        if input("¿Finalizar? (s para sí): ").strip() == 's':
            break

    print(f"\nRecaudación total: ${total_recaudado:,.0f}")

# Ejecutar directo
if __name__ == "__main__":
    ejecutar_sistema()
