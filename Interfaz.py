#Importamos tkinter y logica
import tkinter as tk
import Lógica


#Colores que se usaran en la interfaz
blanco = "#ffffff"
tar = "#f1e8fc"
tar_oscuro = "#e4d6f7"
prim = "#7c4dbd"
prim_oscuro = "#5b3b8c"
prim_claro = "#9b6fd1"

c_titulo = "#3d2266"
c_subt = "#8c6fc4"
c_mut = "#a99bc9"

c_bg = "#aee9c9"
c_fg = "#1e7d4f"
i_bg = "#f7c9a0"
i_fg = "#b3551b"
n_bg = "#ded3f2"
n_fg = "#6b4e9c"

c_ganar = "#d9f4e6"
c_perder = "#fbdede"
c_neutral = "#ededf0"


#Tipografías
t_titulo = ("Segoe UI", 28, "bold")
t_subt = ("Segoe UI", 12)
t_label = ("Segoe UI", 10, "bold")
t_btn = ("Segoe UI", 12, "bold")
t_palabras = ("Segoe UI", 30, "bold")
t_teclado= ("Segoe UI", 11, "bold")


#Ventana principal que maneja el estado de configuración y del juego
class ahorcado (tk.Tk):
    
    def __init__ (self):
        super ().__init__()
        self.title ("El ahorcado")     #Nombre de la ventana
        self.geometry ("680x780")      #Tamaño de la ventana
        self.resizable (True, True)  
        self.configure (bg = blanco)   #Color de ventana
        
        #Cargamos las palabras
        self.palabras = Lógica.cargar_palabras("Palabras.json")
        
        #Preparamos la configuración por defeto
        self.nombre = ""
        self.idioma = "es"
        self.categoria = "animales"
        self.dificultad = "normal"
        self.max_intentos = 6
        
        #Estado de la partida actual
        self.estado = None
        self.frame_actual = None
        
        self.pantalla_bienvenida()
    
    #Funcion para cambiar de panatalla
    def cambiar_ventana (self, frame):
        if self.frame_actual is not None:
            self.frame_actual.destroy ()
        self.frame_actual = frame
        frame.pack (fill = "both", expand = True)
    
    #Pantalla de bienvenida
    def pantalla_bienvenida (self):
        cont = tk.Frame (self, bg = blanco)
        tarjeta = tk.Frame (cont, bg = tar, padx = 60, pady = 45)
        tarjeta.pack (expand = True)
        
        canvas = tk.Canvas (tarjeta, width = 200, height = 210, bg = tar, highlightthickness = 0)
        canvas.pack (pady = (0, 15))
        self.dibujar_bienvenida (canvas)
        
        tk.Label (tarjeta, text = "El Ahorcado", font = t_titulo, bg = tar, fg = c_titulo).pack ()
        tk.Label (
            tarjeta,
            text = "Adivina la palabra letra por letra antes de que sea demasiado tarde",
            font = t_subt, bg = tar, fg = c_subt, justify = "center"). pack (pady = (10, 30))
        
        tk.Button (
            tarjeta,
            text = "Jugar",
            font = t_btn, bg = prim, fg = blanco,
            activebackground = prim_oscuro, activeforeground = blanco,
            relief = "flat", bd = 0, padx = 45, pady = 14, cursor = "hand2",
            command = self.pantalla_configuracion).pack (pady = (0,20))
        
        tk.Label (
            tarjeta,
            text = "v1.0 Hecho con Python",
            font = ("Segoe UI", 9),
            bg = tar, fg = c_mut).pack ()
        
        self.cambiar_ventana(cont)
    
    #Creamos la "portada"
    def dibujar_bienvenida (self, canvas):
        
        c = prim
        canvas.create_line (40, 195, 40, 20, width = 4, fill = c)
        canvas.create_line (40, 20, 120, 20, width = 4, fill = c)
        canvas.create_line (120, 20, 120, 45, width = 4, fill = c)
        canvas.create_line (10, 195, 170, 195, width = 4, fill = c)
        
        canvas.create_oval (100, 45, 140, 85, width = 3, fill = c)
        canvas.create_oval (108, 58, 112, 62, width = 3, fill = c)
        canvas.create_oval (128, 58, 132, 62, width = 3, fill = c)
        canvas.create_arc (106, 58, 132, 80, start = 200, extent = 140, style = "arc", width = 3, outline = c)
        
        canvas.create_line (120, 85, 120, 138, width = 3, fill = c)
        canvas.create_line (120, 95, 95, 120, width = 3, fill = c)
        canvas.create_line (120, 95, 145, 120, width = 3, fill = c)
        canvas.create_line (120, 138, 100, 173, width = 3, fill = c)
        canvas.create_line (120, 138, 140, 173, width = 3, fill = c)
    
    #Pantalla de configuración
    def pantalla_configuracion (self):
        #Creamos la ventana
        cont = tk.Frame (self, bg = blanco)
        
        #Añadimos las etiquetas con el texto inicial
        tk.Label (cont, text = "El Ahorcado", font = ("Segoe UI", 24, "bold"),
                  bg = blanco, fg = c_titulo). pack (pady = (30, 0))
        tk.Label (cont, text = "Configuración", font = t_subt,
                  bg = blanco, fg = c_subt). pack (pady = (0,20))
        
        tarj = tk.Frame (cont, bg = tar, padx = 40, pady = 30)
        tarj.pack (padx = 40, fill = "x")
        
        #tenía un bug debido al desorden de código, llamo pero está escrito más abajo
        self.btns_idioma = {}
        self.btns_categoria = {}
        self.btns_dificultad = {}
        
        #Nombre
        tk.Label (tarj, text = "TU NOMBRE", font = t_label, bg = tar, fg = c_subt).pack (anchor = "w")
        
        self.entry_nombre = tk.Entry (tarj, font = ("Segoe UI", 12), relief = "flat", bd = 8)
        self.entry_nombre.pack (fill = "x", pady = (5, 20))
        self.entry_nombre.insert (0, self.nombre)
        
        #Idioma
        tk.Label (tarj, text = "IDIOMA", font = t_label, bg = tar, fg = c_subt).pack (anchor = "w")
        
        fila_idioma = tk.Frame (tarj, bg = tar)
        fila_idioma.pack (fill = "x", pady = (5, 20))
        
        self.btns_idioma = {}
        
        for cod, etiqueta in [("es", "es Español"), ("en", "is English")]:
            b = tk.Button( fila_idioma, text = etiqueta, font = t_btn, relief = "flat",
                          bd = 0, padx = 20, pady = 10, cursor = "hand2", 
                          command = lambda c = cod: self.elegir_idioma (c))
        
            b.pack (side = "left", padx = (0,10))
        
            self.btns_idioma[cod] = b
        
        #Categoría
        tk.Label (tarj, text = "CATEGORÍA DE PALABRAS", font = t_label,
                  bg = tar, fg = c_subt). pack (anchor = "w")
        
        self.fila_categoria = tk.Frame (tarj, bg = tar)
        self.fila_categoria.pack (fill = "x", pady = (5, 20))
        
        self.btns_categoria = {}
        
        self.construir_categorias ()
        
        #dificultad
        tk.Label (tarj, text = "DIFICULTAD", font = t_label,
                  bg = tar, fg = c_subt). pack (anchor = "w")
        
        fila_dif = tk.Frame (tarj, bg = tar)
        fila_dif.pack (fill = "x", pady = (5, 0))
        
        self.btns_dificultad = {}
        
        for clave, emoji, etiqueta, intentos in [  ("facil", "😊", "Fácil", 8),
            ("normal", "🙂", "Normal", 6),
            ("dificil", "💀", "Difícil", 4)]:
            
            b = tk.Button ( fila_dif, text = f"{emoji}\n{etiqueta}\n{intentos} intentos",
                           font = t_btn, relief = "flat", bd = 0, padx = 20, pady = 15,
                           cursor = "hand2", justify = "center",
                           command = lambda c = clave, i = intentos: self.elegir_dificultad (c, i))
            b.pack (side = "left", padx = (0, 10), fill = "x", expand = True)
            
            self.btns_dificultad [clave] = b
            
        tk.Button (cont, text = "Jugar", font = t_btn,
                       bg = prim, fg = blanco, activebackground = prim_oscuro, activeforeground = blanco,
                       relief = "flat", bd = 0, padx = 45, pady = 14, cursor = "hand2",
                       command = self.iniciar_partida). pack (pady = 30)
            
        self.actualizar_estilos_config ()
        self.cambiar_ventana(cont)
            
    def elegir_idioma (self, codigo):
        self.idioma = codigo
        self.construir_categorias ()
        self.actualizar_estilos_config ()
        
    def construir_categorias (self):
        for w in self.fila_categoria.winfo_children ():
            w.destroy ()
                
        self.btns_categoria = {}
            
        if self.idioma == "es":
            opciones = [
                ("animales", "Animales", "🐾"),
                ("países", "Países", "🌍"),
                ("frutas", "Frutas", "🍎")]
        else:
            opciones = [
                ("animals", "Animals", "🐾"),
                ("countries", "Countries", "🌍"),
                ("fruits", "Fruits", "🍎")]
                
        opciones.append(("aleatorio", "Aleatorio", "🎲"))
            
        claves_validas = [o[0] for o in opciones]
            
        if self.categoria not in claves_validas:
            self.categoria = claves_validas[0]
            
        for clave, etiqueta, emoji in opciones:
            b = tk.Button ( self.fila_categoria, text = f"{emoji}\n{etiqueta}",
                               font = t_btn, relief = "flat", bd = 0, padx = 15,
                               pady = 15, cursor = "hand2", justify = "center",
                               command = lambda c = clave: self.elegir_categoria (c))
            b.pack (side = "left", padx = (0, 10), fill = "x", expand = True)
                
            self.btns_categoria [clave] = b
            
        self.actualizar_estilos_config ()
            
    def elegir_categoria (self, clave):
        self.categoria = clave
        self.actualizar_estilos_config ()
            
    def elegir_dificultad (self, clave, intentos):
        self.dificultad = clave
        self.max_intentos = intentos
        self.actualizar_estilos_config ()
            
    def actualizar_estilos_config (self):
                
        for cod, b in self.btns_idioma.items ():
            sel = cod == self.idioma
            b.configure (
                bg = prim if sel else "white",
                fg = blanco if sel else c_titulo,
                highlightbackground = prim if sel else tar_oscuro,
                highlightthickness = 2
                )
                
        for clave, b in self.btns_categoria.items ():
            sel = clave == self.categoria
            b.configure (
                bg = prim if sel else "white",
                fg = blanco if sel else c_titulo,
                highlightbackground = prim if sel else tar_oscuro,
                highlightthickness = 2
                )
                
        for clave, b in self.btns_dificultad.items ():
            sel = clave == self.dificultad
            b.configure (
                bg = prim if sel else "white",
                fg = blanco if sel else c_titulo,
                highlightbackground = prim if sel else tar_oscuro,
                highlightthickness = 2
                )
                    
    #toma los daros y genera una partida con la configuracion
    def iniciar_partida (self):
        self.nombre = self.entry_nombre.get().strip () or "Jugador"
        self.generar_partida ()
            
    #Genera una palabra nueva y reinicia estado manteniendo la configuracion actual
    def generar_partida (self):
        palabra = Lógica.elegir_palabra(self.palabras, self.idioma, self.categoria)
        self.estado = Lógica.nuevo_juego (palabra, self.max_intentos)
        self.mostrar_juego ()
        
    
    #pantalla de juego y resultado
    def mostrar_juego (self):
        self.title (f"El Ahorcado - {self.nombre}")
        
        cont = tk.Frame (self, bg = tar)
        
        tk.Label (cont, text = "El Ahorcado", font = ("Segoe UI", 20, "bold"),
                  bg = tar, fg = c_titulo). pack (pady = (20,10))
        
        #Dibujo del ahorcado
        self.zona_superior = tk.Frame (cont, bg = tar_oscuro, height=230)
        self.zona_superior. pack (fill = "x", padx = 40, pady = (0, 15))

        self.lbl_palabra = tk.Label(cont, font = t_palabras, bg = tar, fg = c_titulo)
        self.lbl_palabra. pack (pady = (5, 5))

        self.lbl_incorrectas = tk.Label (cont, font = t_subt, bg = tar, fg = i_fg)
        self.lbl_incorrectas. pack (pady = (0, 15))

        self.frame_teclado = tk.Frame (cont, bg=tar)
        self.frame_teclado. pack (pady = (0, 10))
        
        #Barra inferior con botones e info
        barra = tk.Frame (cont, bg = tar_oscuro)
        barra.pack (fill = "x", side = "bottom")
        
        self.lbl_intentos = tk.Label (barra, font = t_label, bg = tar_oscuro, fg = c_titulo)
        self.lbl_intentos.pack (side = "left", padx = 20, pady = 15)
        
        self.btn_nueva = tk.Button (barra, text = "Nueva partida", font = t_btn,
                                    bg = prim_oscuro, fg = blanco, relief = "flat",
                                    bd = 0, padx = 15, cursor = "hand2",
                                    command = self.generar_partida)
        self.btn_nueva.pack (side = "right", padx = 20, pady = 10)
        
        self.btn_adivinar = tk.Button (barra, text = "Adivinar", font = t_btn, bg = prim_claro, fg = blanco,
                                       relief = "flat", bd = 0, padx = 15, pady = 8, cursor = "hand2",
                                       command = self.abrir_adivinar)
        self.btn_adivinar.pack (side = "right", padx = (10, 10), pady = 10)
        
        self.btn_config = tk.Button (barra, text = "Configuración", font = t_btn, bg = blanco, fg = c_titulo,
                                     relief = "flat", bd = 0, padx = 15, pady = 8, cursor = "hand2",
                                     command = self.pantalla_configuracion)
        self.btn_config.pack (side = "right", padx = (10, 0), pady = 10)
        
        self.construir_teclado ()
        self.actualizar_juego ()
        self.cambiar_ventana (cont) 
        
    def construir_teclado (self):
        for w in self.frame_teclado.winfo_children ():
            w.destroy ()
        self.botones_letras = {}
        
        letras = list ("ABCDEFGHIJKMN")
        if self.idioma == "es":
            letras.append ("Ñ")
        letras += list ("LOPQRSTUVWXYZ")
        
        n = len (letras)
        tam_fila = - (-n // 3)
        filas = [letras[i:i + tam_fila] for i in range (0, n, tam_fila)]
        
        for fila in filas:
            fila_frame = tk.Frame (self.frame_teclado, bg = tar)
            fila_frame.pack (pady = 4)
            
            for letra in fila:
                b = tk.Button (fila_frame, text = letra, font = t_teclado,
                               width = 3, height = 1, relief = "flat", bd = 0,
                               cursor = "hand2", bg = n_bg, fg = n_fg,
                               command = lambda l = letra: self.click_letra(l))
                b.pack (side = "left", padx = 3)
                
                self.botones_letras [letra] = b
    def click_letra (self, letra):
        if self.estado ["terminado"]:
            return
        self.estado = Lógica.adivinar_letra(self.estado, letra)
        self.actualizar_juego ()
    
    def actualizar_juego (self):
        estado = self.estado
        
        self.lbl_palabra.configure (text = " ".join (Lógica.letras_correctas_visibles(estado)))
        
        if estado ["letras_incorrectas"]:
            texto = "Letras incorrectas: " + ", ".join (sorted (estado ["letras_incorrectas"]))
        else:
            texto = ""
            
        self.lbl_incorrectas.configure (text = texto)
        
        self.lbl_intentos.configure (text = f"Intentos restantes: {estado['intentos_restantes']}")
        
        for letra, b in self.botones_letras.items ():
            if letra in estado ["letras_correctas"]:
                b.configure (bg = c_bg, fg = c_fg, state = "disabled")
            elif letra in estado ["letras_incorrectas"]:
                b.configure (bg = i_bg, fg = i_fg, state = "disabled")
            else:
                b.configure (bg = n_bg, fg = n_fg, state = "disabled"
                             if estado ["terminado"] else "normal")
        
        for w in self.zona_superior.winfo_children ():
            w.destroy ()
        
        if estado ["terminado"]:
            self.mostrar_resultado ()
            self.btn_adivinar.pack_forget ()
        else:
            errores = len (estado ["letras_incorrectas"])
            canvas = tk.Canvas (self.zona_superior, width = 700, height = 230,
                                bg = tar_oscuro, highlightthickness = 0)
            
            canvas.pack ()
            
            self.dibujar_ahorcado (canvas, errores, estado ["max_intentos"])
            
            if not self.btn_adivinar.winfo_ismapped ():
                self.btn_adivinar.pack (side = "right", padx = (10, 10), pady = 10)
        
    def mostrar_resultado (self):
        estado = self.estado
        gano = estado ["gano"]
    
        fila = tk.Frame (self.zona_superior, bg = tar_oscuro)
        fila.pack (fill = "both", expand = True, padx = 10, pady = 10)
    
        color_fondo = c_ganar if gano else c_perder
        color_texto = c_fg if gano else i_fg
    
        ventana = tk.Frame (fila, bg = color_fondo, padx = 30, pady = 25)
        ventana.pack (expand = True)
    
        if gano:
            tk.Label (ventana, text = "🎉", font = ("Segoe UI", 32), bg = color_fondo).pack ()
            tk.Label (ventana, text = "¡Ganaste!", font = t_btn,
                 bg = color_fondo, fg = color_texto).pack (pady = (5, 0))
            tk.Label (ventana, text = f"La palabra era {estado['palabra']}", font = t_subt,
                 bg = color_fondo, fg = color_texto).pack ()
        else:
            tk.Label (ventana, text = "😔", font = ("Segoe UI", 32), bg = color_fondo).pack ()
            tk.Label (ventana, text = "¡Perdiste!", font = t_btn,
                 bg = color_fondo, fg = color_texto).pack (pady = (5, 0))
            tk.Label (ventana, text = f"Era: {estado['palabra']}", font = t_subt,
                 bg = color_fondo, fg = color_texto, justify = "center").pack ()
    
    #dibujar al ahorcado segun la cantidad de intentos
    def dibujar_ahorcado (self, canvas, errores, max_intentos):
        c = prim_oscuro
        cx, cy = 350, 115
    
        #La horca siempre visible
        canvas.create_line(cx - 80, cy + 95, cx - 80, cy - 95, width=4, fill=c)
        canvas.create_line(cx - 80, cy - 95, cx, cy - 95, width=4, fill=c)
        canvas.create_line(cx, cy - 95, cx, cy - 65, width=4, fill=c)
        canvas.create_line(cx - 110, cy + 95, cx + 50, cy + 95, width=4, fill=c)
        
        partes_totales = 6
        
        proporcion = errores / max_intentos if max_intentos else 0
        partes = min (partes_totales, round (proporcion * partes_totales))
        
        if partes >= 1:  # Cabeza
           canvas.create_oval(cx - 20, cy - 65, cx + 20, cy - 25, width=3, outline=c)
        if partes >= 2:  # Cuerpo
           canvas.create_line(cx, cy - 25, cx, cy + 30, width=3, fill=c)
        if partes >= 3:  # Brazo izquierdo
           canvas.create_line(cx, cy - 15, cx - 25, cy + 10, width=3, fill=c)
        if partes >= 4:  # Brazo derecho
           canvas.create_line(cx, cy - 15, cx + 25, cy + 10, width=3, fill=c)
        if partes >= 5:  # Pierna izquierda
           canvas.create_line(cx, cy + 30, cx - 20, cy + 65, width=3, fill=c)
        if partes >= 6:  # Pierna derecha
           canvas.create_line(cx, cy + 30, cx + 20, cy + 65, width=3, fill=c)
    
    #Adivinar palabra completa
    def abrir_adivinar(self):
        modal = tk.Toplevel(self)
        modal.title("")
        modal.configure(bg="white")
        modal.geometry("380x230")
        modal.resizable(False, False)
        modal.transient(self)
        modal.grab_set()
 
        tk.Label (modal, text = "Adivinar palabra", font=("Segoe UI", 16, "bold"),
                 bg="white", fg = c_titulo).pack(pady=(20, 5))
        tk.Label (modal, text= "Si fallas, perderás la partida.", font=t_subt ,
                 bg="white", fg = c_subt).pack()
 
        entry = tk.Entry(modal, font=("Segoe UI", 12), justify="center", relief="flat", bd=8)
        entry.pack(pady=20, padx=40, fill="x")
        entry.focus_set()
 
        botones = tk.Frame(modal, bg="white")
        botones.pack(pady=(0, 10))
 
        def confirmar():
            intento = entry.get().strip()
            if intento:
                self.estado = Lógica.adivinar_palabra(self.estado, intento)
                self.actualizar_juego()
            modal.destroy()
 
        tk.Button(botones, text="Cancelar", font= t_btn , bg="white", fg= c_titulo ,
                  relief="flat", bd=1, padx=20, pady=8, cursor="hand2",
                  command=modal.destroy).pack(side="left", padx=10)
        tk.Button(botones, text="Confirmar", font= t_btn , bg= prim_oscuro , fg="white",
                  relief="flat", bd=0, padx=20, pady=8, cursor="hand2",
                  command=confirmar).pack(side="left", padx=10)
 
        entry.bind("<Return>", lambda e: confirmar())

if __name__ == "__main__":
    app = ahorcado()
    app.mainloop()