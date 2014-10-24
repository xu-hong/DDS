#simulate fake data 
x_1 <- rnorm(1000, 5, 7)

hist(x_1, col="Grey")
true_error <- rnorm(1000, 0, 2)
true_beta_0 <- 1.1
true_beta_1 <- -8.2
y <- true_beta_0 + true_beta_1*x_1 + true_error
hist(y)
plot(x_1, y, pch=20, col="red")


#build a linear regression model
model <- lm(y ~ x_1)
coefs <- coef(model)
abline(coefs[1], coefs[2])

#add another variable
x_2 <- rgamma(1000, 0.1)
true_beta_2 <- 5
yy <- true_beta_0 + true_beta_1*x_1 + true_beta_2*x_2 + true_error

#
model1 <- lm(yy~x_1)
model2 <- lm(yy~x_2)
model12 <- lm(y~x_1+x_2)
