# ConversorTemperatura

Conversor de Temperatura desenvolvido em Python.

1. Solicitando uma temperatura para o usuário;
2. Solicitando a unidade de medida de temperatura para o usuário;
3. São possíveis 3 entradas :
      [1] Corresponde a unidade de medida Celsiu
      [2] Corresponde a unidade de medida Fahrenheit
      [3] Corresponde a unidade de medida Kelvin
4. Assim que o usuário escolhe a unidade de medida, é solicitado para qual unidade de medida deseja converter.
5. Supondo que o usuário escolha Celsius como unidade de medida, será possível converter para Fahrenheit e Kelvin.
6. Supondo que o usuário escolha Fahrenheit como unidade de medida, será possível converter para Celsius e Kelvin.
7. Supondo que o usuário escolha Kelvin como unidade de medida, será possível converter para Celsius e Fahrenheit.
8. Fórmulas utilizadas na conversão :

   Celsius -> Fahrenheit : (0 °C × 9/5) + 32 = 32 °F
   
   Celsius -> Kelvin : 0 °C + 273,15 = 273,15 K
   
   --------------------------------------------
   
   Fahrenheit -> Celsius : (0 °F − 32) × 5/9 = -17,78 °C
   
   Fahrenheit -> Kelvin : (0 °F − 32) × 5/9 + 273,15 = 255,372 K
   
   --------------------------------------------
   
   Kelvin -> Celsius : 0 K − 273,15 = -273,1 °C
   
   Kelvin -> Fahrenheit : (0 K − 273,15) × 9/5 + 32 = -459,7 °F
   
   --------------------------------------------
   
10. Por fim é mostrado ao usuário a conversão da temperatura para a unidade de medida solicitada.
