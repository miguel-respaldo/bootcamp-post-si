#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import math

class FiguraGeometrica:

    def __init__(self, nombre="N/A", lados=0):
        self.nombre = nombre
        self.lados = lados
        self.area = 0
        self.perimetro = 0

    def get_nombre(self):
        print("Nombre:", self.nombre)


class Triangulo(FiguraGeometrica):

    def __init__(self, tipo="equilatero"):
        FiguraGeometrica.__init__(self, "triangulo", 3)
        self.tipo = tipo

class Circulo(FiguraGeometrica):

    def __init__(self, radio=0):
        super().__init__(self, "circulo", 0)
        self.radio = radio

    def get_area():
        return math.pi * radio * radio

class Cuadrado(FiguraGeometrica):
    pass


tr = Triangulo("escaleno")
ci = Circulo("circulo", 0)
cu = Cuadrado("cuadrado", 4)

tr.get_nombre()
ci.get_nombre()
cu.get_nombre()



