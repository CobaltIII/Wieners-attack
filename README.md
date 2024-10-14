# Wieners-attack
A demonstation of Wiener's Attack against RSA in the case of a small private exponent with the concept of continued fractions.

### Continued fractions and Convergents
for $\alpha \in \mathbb{R}^+$ , for $c_i \in \mathbb{N}$

$$\\ \alpha = c_0 + \frac{1}{c_1 + \frac{1}{c_2 + \frac{1}{c_3 + ...}}} = [c_0 ; c_1 , c_2 , c_3 , ... ]$$

The nth convergent of $\alpha = [c_0 ; c_1 , c_2 , c_3 , ... ] \in \mathbb{R}^+$ is 

$$\frac{a_n}{b_n} = [c_0 ; c_1 , c_2 , c_3 , ...  , c_n]$$

Identity of convergents - Convergents are a "best" approximation of $\alpha$ for a given $b_n$ , that is

$$\|\alpha - \frac{a_n}{b_n}\| < \|\alpha - \frac{a}{b}\| \text{for all } \frac{a}{b} \in \mathbb{Q} \text{with } \frac{a}{b} \neq \frac{a_n}{b_n} \text{ and } b \leq b_n$$


#### Weiner's Theorem - 
A property of continued fractions where $\alpha \in \mathbb{R} , a,b \in \mathbb{Z}$ such that, $\|\alpha - \frac{a}{b}\| < \frac{1}{2b^2}$ , then $\frac{a}{b}$ is a convergent of the expansion of $\alpha$


