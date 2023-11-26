package Parcial3;

public class Chef {
    public synchronized void producirPlato(int cantidad, String plato) {
        // Lógica para producir el plato
        System.out.println("Chef produjo " + cantidad + " platos de " + plato);
        // Llamar a Main para notificar que hay un plato listo
        Main.notificarPlatoListo(cantidad, plato);
    }
}
