def ejecutar_sistema():
    # 1. INICIALIZACIÓN: Definimos las variables para capacidad (c_), 
    # vendidos (v_) y precio (p_) de forma independiente por sector.
    c_vip, v_vip, p_vip = 500, 0, 250000
    c_gral, v_gral, p_gral = 5000, 0, 150000
    c_pref, v_pref, p_pref = 1500, 0, 180000
    c_baj, v_baj, p_baj = 2500, 0, 130000
    c_alt, v_alt, p_alt = 3000, 0, 100000
    c_pop, v_pop, p_pop = 5000, 0, 70000

    # 2. CONTADORES GLOBALES: Seguimos el total de dinero y de tickets.
    total_recaudado = 0
    total_entradas = 0
    
    # 3. BUCLE PRINCIPAL: Permite realizar múltiples ventas hasta que el usuario decida salir.
    while True:
        print("\n--- SELECCIONE SECTOR ---")
        # Mostramos la capacidad disponible restando los vendidos a la capacidad total.
        print(f"1. Campo VIP (Disp: {c_vip - v_vip}) | 2. Campo General (Disp: {c_gral - v_gral})")
        print(f"3. Platea Pref. (Disp: {c_pref - v_pref}) | 4. Platea Baja (Disp: {c_baj - v_baj})")
        print(f"5. Platea Alta (Disp: {c_alt - v_alt}) | 6. Popular (Disp: {c_pop - v_pop})")
        
        opc_s = input("Opción: ").strip()
        precio_base = 0
        
        # 4. PROCESO DE VENTA: Verificamos si hay stock antes de incrementar vendidos.
        if opc_s == "1" and v_vip < c_vip: v_vip += 1; precio_base = p_vip
        elif opc_s == "2" and v_gral < c_gral: v_gral += 1; precio_base = p_gral
        elif opc_s == "3" and v_pref < c_pref: v_pref += 1; precio_base = p_pref
        elif opc_s == "4" and v_baj < c_baj: v_baj += 1; precio_base = p_baj
        elif opc_s == "5" and v_alt < c_alt: v_alt += 1; precio_base = p_alt
        elif opc_s == "6" and v_pop < c_pop: v_pop += 1; precio_base = p_pop
        else:
            print("¡Error! Sector inválido o lleno."); continue
            
        # 5. APLICACIÓN DE DESCUENTO: Calculamos la tasa según la opción elegida.
        desc = input("Descuento (1.Anticipado, 2.Preventa, 3.Pack, 4.Nada): ").strip()
        tasa = 0.35 if desc=="1" else 0.15 if desc=="2" else 0.23 if desc=="3" else 0
        
        # 6. CÁLCULO FINAL: Aplicamos el descuento al precio y sumamos a los acumuladores.
        precio_final = precio_base * (1 - tasa)
        total_recaudado += precio_final
        total_entradas += 1
        
        print(f"Venta confirmada: ${precio_final:,.0f}")
        
        if input("¿Cerrar programa y ver informe? (s/n): ").strip() == 's': break

    # 7. INFORME DE ESTADÍSTICAS: Se ejecuta al terminar el bucle.
    print("\n--- INFORME DE VENTAS ---")
    print(f"Entradas totales vendidas: {total_entradas}")
    print(f"Total recaudado: ${total_recaudado:,.0f}")
    
    # 8. CÁLCULO DEL MÁS DEMANDADO: Comparamos manualmente los contadores.
    max_ventas = v_vip
    mejor_sector = "Campo VIP"
    if v_gral > max_ventas: max_ventas = v_gral; mejor_sector = "Campo General"
    if v_pref > max_ventas: max_ventas = v_pref; mejor_sector = "Platea Preferencial"
    if v_baj > max_ventas: max_ventas = v_baj; mejor_sector = "Platea Baja"
    if v_alt > max_ventas: max_ventas = v_alt; mejor_sector = "Platea Alta"
    if v_pop > max_ventas: max_ventas = v_pop; mejor_sector = "Popular"
    
    print(f"Sector más demandado: {mejor_sector} ({max_ventas} entradas)")
    
    # 9. PAUSA: Evita que la ventana se cierre sola.
    input("\nPresiona Enter para cerrar la ventana...")

# Ejecución del programa
if __name__ == "__main__":
    ejecutar_sistema()
