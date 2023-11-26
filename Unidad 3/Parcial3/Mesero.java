package Parcial3;

public class Mesero {
    public synchronized void consumirPedido(int cantidad, String plato) {
        // Lógica para consumir el pedido
        System.out.println("Mesero consumió " + cantidad + " platos de " + plato);
        // Llamar a Main para notificar que se ha consumido un plato
        Main.notificarPlatoConsumido(cantidad, plato);
    }
}

