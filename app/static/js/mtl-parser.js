export class MTLParser {
    /**
     * Parses MTL file content and extracts material definitions and texture maps
     * @param {string} text - The raw text of the .mtl file
     * @returns {Object[]} List of material objects { name, maps: {}, props: {} }
     */
    static parse(text) {
        const materials = [];
        const lines = text.split('\n');
        let currentMaterial = null;

        const mapPrefixes = {
            'map_kd': 'base_color_map',
            'map_kn': 'normal_map',
            'map_ks': 'roughness_map', // Often used for specular/roughness in OBJ
            'map_ns': 'roughness_map',
            'map_pr': 'roughness_map',
            'map_pm': 'metallic_map',
            'map_bump': 'normal_map',
            'bump': 'normal_map',
            'norm': 'normal_map',
            'disp': 'displacement_map',
            'map_disp': 'displacement_map',
            'map_ka': 'ao_map',
            'map_ao': 'ao_map'
        };

        for (let line of lines) {
            line = line.trim().replace(/\s+/g, ' ');
            if (line.startsWith('#') || !line) continue;

            const parts = line.split(' ');
            const command = parts[0].toLowerCase();

            if (command === 'newmtl') {
                currentMaterial = {
                    name: parts.slice(1).join(' '),
                    maps: {},
                    props: {},
                    diffuse: [0.8, 0.8, 0.8, 1.0]
                };
                materials.push(currentMaterial);
            } else if (currentMaterial) {
                if (mapPrefixes[command]) {
                    // Extract full path, then get basename
                    let fullPath = parts.slice(1).join(' ');
                    // Remove common MTL options like -bm 1.0, -s 1 1 1, etc.
                    // This is a simple regex to find the last part that looks like a filename/path
                    let filename = fullPath.split(' ').filter(p => !p.startsWith('-')).pop();
                    if (filename) {
                        filename = filename.replace(/\\/g, '/').split('/').pop();
                        currentMaterial.maps[mapPrefixes[command]] = filename;
                    }
                } else if (command === 'kd') {
                    // Diffuse color: Kd R G B
                    const r = parseFloat(parts[1]) || 0.8;
                    const g = parseFloat(parts[2]) || 0.8;
                    const b = parseFloat(parts[3]) || 0.8;
                    currentMaterial.diffuse = [r, g, b, 1.0];
                }
            }
        }
        
        return materials;
    }

    /**
     * Legacy method for compatibility - just returns names
     */
    static parseMaterialNames(text) {
        return this.parse(text).map(m => m.name);
    }
}
