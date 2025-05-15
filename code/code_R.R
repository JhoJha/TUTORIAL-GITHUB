
set.seed(42)
horas_estudio = runif(50, min = 0, max = 10)
ruido = rnorm(50, mean = 0, sd = 3)
calificacion <- 2.5 * horas_estudio + ruido

datos <- data.frame(horas_estudio, calificacion)

modelo <- lm(calificacion ~ horas_estudio, data = datos)

summary(modelo)

plot(datos$horas_estudio, datos$calificacion,
     main = "Regresión Lineal Simple",
     xlab = "Horas de estudio", ylab = "Calificación",
     pch = 19, col = "blue")
abline(modelo, col = "red", lwd = 2)











