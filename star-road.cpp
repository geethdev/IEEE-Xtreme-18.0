#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN];       
vector<int> calificaciones;   // Calificaciones de restaurantes en cada ciudad
vector<bool> visitado(MAXN);  // Seguimiento de ciudades visitadas

// Función para calcular la longitud de la LIS para una secuencia dada de calificaciones
int calcularLIS(const vector<int>& estrellas) {
    vector<int> lis;
    for (int calificacion : estrellas) {
        auto it = upper_bound(lis.begin(), lis.end(), calificacion);
        if (it == lis.end()) {
            lis.push_back(calificacion);  // Extender LIS
        } else {
            *it = calificacion;  // Reemplazar para mantener un final posible más bajo
        }
    }
    return lis.size();  // Longitud de LIS
}

void dfs(int ciudad, vector<int>& camino, int& maxRestaurantes) {
    visitado[ciudad] = true;
    camino.push_back(calificaciones[ciudad]);

    maxRestaurantes = max(maxRestaurantes, calcularLIS(camino));

    // Recorrer vecinos
    for (int vecino : adj[ciudad]) {
        if (!visitado[vecino]) {
            dfs(vecino, camino, maxRestaurantes);
        }
    }

    // Retroceder
    camino.pop_back();
    visitado[ciudad] = false;
}

int main() {
    int N;
    cin >> N;
    calificaciones.resize(N + 1);

    // Entrada de calificaciones de estrellas para cada ciudad
    for (int i = 1; i <= N; ++i) {
        cin >> calificaciones[i];
    }

    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int maxRestaurantes = 0;
    vector<int> camino;

    for (int i = 1; i <= N; ++i) {
        fill(visitado.begin(), visitado.end(), false);
        dfs(i, camino, maxRestaurantes);
    }

    cout << maxRestaurantes << endl;
    return 0;
}