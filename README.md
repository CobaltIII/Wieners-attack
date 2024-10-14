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

### Proof - 

Let there exist some $k \in \mathbb{Z}$ with $ed - k \phi(N) = 1$ so
dividing both sides by $d \phi(N)$, we get

$$ \\ \| \frac{e}{\phi(N)} - \frac{k}{d} \| = \| \frac{1}{d\phi(N)}\| \implies \frac{e}{\phi(N)} \text{  approximates to   } \frac{k}{d}$$

Since $\phi(N)$ is private, we can use N instead, why?

$\| N - \phi(N) \| = \| N - (p-1)(q-1) \| = \| p + q - 1 \| < 3\sqrt{N}$ so

$\| \frac{e}{N} - \frac{k}{d} \| =  \| \frac{ed - k \phi(N) - kN + k\phi(N)}{Nd}\| = \| \frac{1 - k(N - \phi(N))}{Nd}\| \leq \| \frac{3k\sqrt{N}}{Nd} \| = \frac{3k}{d\sqrt{N}} $

We know $k \phi(N) = ed - 1 < ed$. Since $e < \phi(N)$, we see $k < d < \frac{N^{1/4}}{3}$

Thus we can prove that the the private key d will appear as the the denominator of some convergent of e/N.

Thus using the approximation and substituting k, we get

$$ \\ \| \frac{e}{\phi(N)} - \frac{k}{d} \| \leq \frac{1}{dN^{1/4}}  ( \text{ now, substituting } N^{1/4} \text{ as 3d } ) < \frac{1}{3d^2} < \frac{1}{2d^2}$$

