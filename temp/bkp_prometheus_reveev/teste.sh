#!/bin/bash

BASE_IP="192.168.100.248"
START_PORT=3031
END_PORT=3047

fetch_and_save() {
    local port=$1

    if [ "$port" -gt "$END_PORT" ]; then
        return
    fi

    local url="http://${BASE_IP}:${port}/equipamento/config/"
    local file="config_port_${port}.txt"

    echo "Consultando porta ${port}..."

    if curl -s --fail --connect-timeout 5 "$url" -o "$file"; then
        echo "[OK] Porta ${port} → salvo em ${file}"
    else
        echo "[ERRO] Porta ${port}"
        rm -f "$file"
    fi

    # chamada recursiva
    fetch_and_save $((port + 1))
}

fetch_and_save "$START_PORT"
