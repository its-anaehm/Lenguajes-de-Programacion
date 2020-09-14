
/comment

    # !Método Factorial.
    # * Permite calcular la multiplicación de n*(n-1)*(n-2)*...*(n-k), donde n-k >=1
    # @author jose.inestroza@unah.edu.hn
    # @version 0.1

uncomment/

# Pruebe para que encuentr la solución en sus propias prácricas.
def factorial n 
    if n<2
        return 1
    end
    n*factorial(n-1)
end

n=5
puts("El factorial en Ruby para '%d' es: '%d'" % [n, factorial(n)])