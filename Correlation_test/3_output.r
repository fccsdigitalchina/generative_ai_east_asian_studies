# Load the data from the CSV file
data <- read.csv("1_task_correlation.csv")

# Calculate the correlation and significance for fff_ro and ff_ro
cor_ff_ro <- cor.test(data$fff_ro, data$ff_ro)

# Print the result
print(cor_ff_ro)

# Calculate the correlation and significance for fff_ro and f_ro
cor_f_ro <- cor.test(data$fff_ro, data$f_ro)

# Print the result
print(cor_f_ro)

# Calculate the correlation and significance for ff_ro and f_ro
cor_ff_f <- cor.test(data$ff_ro, data$f_ro)

# Print the result
print(cor_ff_f)
