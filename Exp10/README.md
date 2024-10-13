# Exp10: Visualize Data Using Any Plotting Framework

## Aim
To visualize data using any plotting framework.

## Program

#### 1) Scatter Plot

```r
# Install ggplot2 (if not already installed)
install.packages("ggplot2")
# Load the ggplot2 package
library(ggplot2)
# Scatter plot of Sepal.Length vs Sepal.Width, colored by Species
ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point(size = 3) + # Adds points
  labs(title = "Scatter Plot of Sepal Dimensions", 
       x = "Sepal Length (cm)", 
       y = "Sepal Width (cm)") + # Adds axis labels and title
```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp10/Images/Screenshot%202024-10-07%20162130.png)

#### 2) Bar Chart

```r
# Install ggplot2 (if not already installed)
install.packages("ggplot2")
# Load the ggplot2 package
library(ggplot2)
# Bar plot of Species counts
ggplot(data = iris, aes(x = Species)) +
  geom_bar(fill = "steelblue") + # Adds bars filled with steel blue color
  labs(title = "Count of Different Species in Iris Dataset", 
       x = "Species", 
       y = "Count") +
  theme_minimal()
```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp10/Images/Screenshot%202024-10-07%20162203.png)

#### 3) Histogram

```r
install.packages("ggplot2")
# Load the ggplot2 package
library(ggplot2)
# Histogram of Sepal Length
ggplot(data = iris, aes(x = Sepal.Length)) +
  geom_histogram(binwidth = 0.3, fill = "orange", color = "black") + # Adds
labs(title = "Histogram of Sepal Length", 
     x = "Sepal Length (cm)", 
     y = "Frequency") +
  theme_minimal()
```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp10/Images/Screenshot%202024-10-07%20162235.png)

#### 4) Box Plot

```r
install.packages("ggplot2")
# Load the ggplot2 package
library(ggplot2)
# Box plot of Sepal Length for each Species
ggplot(data = iris, aes(x = Species, y = Sepal.Length, fill = Species)) +
  geom_boxplot() + # Adds box plot
  labs(title = "Box Plot of Sepal Length by Species", 
       x = "Species", 
       y = "Sepal Length (cm)") +
  theme_minimal()
```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp10/Images/Screenshot%202024-10-07%20162323.png)

## Result

Thus visualized the data using main four plotting frameworks.