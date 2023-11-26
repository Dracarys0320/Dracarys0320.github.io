package Hilos;

public class Hilos {

    private static final int SIZE = 4;

    public static void main(String[] args) {
        // Crear matrices
        int[][] matrix1 = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 16}
        };

        int[][] matrix2 = {
                {17, 18, 19, 20},
                {21, 22, 23, 24},
                {25, 26, 27, 28},
                {29, 30, 31, 32}
        };

        int[][] resultMatrix = new int[SIZE][SIZE];

        // Crear y ejecutar hilos para sumar filas
        Thread[] threads = new Thread[SIZE];

        for (int i = 0; i < SIZE; i++) {
            threads[i] = new Thread(new MatrixRowSumThread(matrix1, matrix2, resultMatrix, i));
            threads[i].start();
        }

        // Esperar a que todos los hilos terminen
        try {
            for (Thread thread : threads) {
                thread.join();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Imprimir la matriz resultante
        System.out.println("Matriz Resultante:");
        printMatrix(resultMatrix);
    }

    private static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int value : row) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
    }
}

class MatrixRowSumThread implements Runnable {

    private final int[][] matrix1;
    private final int[][] matrix2;
    private final int[][] resultMatrix;
    private final int row;

    public MatrixRowSumThread(int[][] matrix1, int[][] matrix2, int[][] resultMatrix, int row) {
        this.matrix1 = matrix1;
        this.matrix2 = matrix2;
        this.resultMatrix = resultMatrix;
        this.row = row;
    }

    @Override
    public void run() {
        for (int i = 0; i < matrix1[row].length; i++) {
            resultMatrix[row][i] = matrix1[row][i] + matrix2[row][i];
        }
    }
}
