package Parcial3;

public class Main {
    private static Chef chef = new Chef();
    private static Mesero mesero = new Mesero();

    public static void main(String[] args) {
        // Crear hilos productores
        Thread chef1 = new Thread(() -> {
            chef.producirPlato(5, "Pasta");
        });

        Thread chef2 = new Thread(() -> {
            chef.producirPlato(3, "Sushi");
        });

        // Crear hilos consumidores
        Thread mesero1 = new Thread(() -> {
            mesero.consumirPedido(2, "Pasta");
        });

        Thread mesero2 = new Thread(() -> {
            mesero.consumirPedido(1, "Sushi");
        });

        // Iniciar los hilos
        chef1.start();
        chef2.start();
        mesero1.start();
        mesero2.start();
    }

    public static void notificarPlatoListo(int cantidad, String plato) {
        // Lógica para manejar la notificación de que un plato está listo
        System.out.println("Plato listo: " + cantidad + " platos de " + plato);
    }

    public static void notificarPlatoConsumido(int cantidad, String plato) {
        // Lógica para manejar la notificación de que un plato ha sido consumido
        System.out.println("Plato consumido: " + cantidad + " platos de " + plato);
    }
}

