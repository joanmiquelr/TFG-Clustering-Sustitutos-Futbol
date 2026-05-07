# Instalar y cargar librerías necesarias
library(MASS)

# Definir parámetros
Sigma <- matrix(c(16, 1.5, 
                  1.5, 0.25), nrow = 2, byrow = TRUE)

mu1 <- c(0, 0)
mu2 <- c(4, 4)

# Simulación de 25 puntos de cada grupo (total 50)
set.seed(123)  # para reproducibilidad
x1 <- mvrnorm(n = 25, mu = mu1, Sigma = Sigma)
x2 <- mvrnorm(n = 25, mu = mu2, Sigma = Sigma)

# Combinar los datos
datos_no_int <- rbind(x1, x2)
intermedios <- matrix(c(2, 2,   # primer punto
                        2.5, 1.5),  # segundo punto
                      ncol = 2, byrow = TRUE)

datos <- rbind(x1, x2, intermedios)
grupo <- c(rep("G1", 25), rep("G2", 25), rep("INT", 2))

# ---- Plot ----
plot(x1, col = "black", pch = 19, xlim = range(datos[,1]), ylim = range(datos[,2]),
     xlab = "X1", ylab = "X2", main = "Simulación con puntos intermedios")
points(x2, col = "red", pch = 19)
points(intermedios, col = "blue", pch = 19, cex = 1.5)

legend("bottomright", legend = c("Grupo 1", "Grupo 2", "Intermedios"),
       col = c("black", "red", "blue"), pch = 19)


D <- dist(datos, method = "euclidean")
D2 <- dist(datos_no_int, method = "euclidean")
hc_single   <- hclust(D, method = "single")
hc_single_5 <- hclust(D2, method = "single")
hc_complete <- hclust(D, method = "complete")
hc_average  <- hclust(D, method = "average")

# ---- Dendrogramas lado a lado ----
plot(hc_single,   main = "Dendrograma - Single",   xlab = "", sub = "")

plot(hc_complete, main = "Dendrograma - Complete", xlab = "", sub = "")

plot(hc_average,  main = "Dendrograma - Average",  xlab = "", sub = "")
par(op)

# ---- (Opcional) Asignaciones con k=2 ----
cl_single   <- cutree(hc_single,   k = 2)
cl_single2  <- cutree(hc_single_5,   k = 5)
cl_complete <- cutree(hc_complete, k = 4)
cl_average  <- cutree(hc_average,  k = 4)

# Para comparar visualmente uno de los métodos:
par(mfrow = c(2, 2))  # 2 filas, 2 columnas

plot(datos, col = cl_single, pch = 19,
     main = "Método Simple", xlab = "X1", ylab = "X2")
legend("bottomright", legend = paste("Cluster", 1:2), col = 1:2, pch = 19)

plot(datos, col = cl_single2, pch = 19,
     main = "Método Simple (5 clusters)", xlab = "X1", ylab = "X2")
legend("bottomright", legend = paste("Cluster", 1:5), col = 1:5, pch = 19)

plot(datos, col = cl_complete, pch = 19,
     main = "Método Completo", xlab = "X1", ylab = "X2")
legend("bottomright", legend = paste("Cluster", 1:4), col = 1:4, pch = 19)


plot(datos, col = cl_average, pch = 19,
     main = "Método Promedio", xlab = "X1", ylab = "X2")
legend("bottomright", legend = paste("Cluster", 1:4), col = 1:4, pch = 19)

