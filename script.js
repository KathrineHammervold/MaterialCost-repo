document.getElementById('loadData').addEventListener('click', function() {
    // Call the REST API to get the different house parts, and the materials available for each part
    fetch('http://127.0.0.1:5000/get_house_parts')
        .then(response => response.json())
        .then(data => {
            console.log('Data received:', data);
            const tableBody = document.getElementById('dataTable').getElementsByTagName('tbody')[0];
            tableBody.innerHTML = ''; // Clear existing data

            data.forEach(item => {
                const row = tableBody.insertRow();
                row.insertCell(0).textContent = item.Part;
                
                const materialCell = row.insertCell(1);
                const materialSelect = document.createElement('select');
                materialSelect.innerHTML = `
                    <option value="" disabled selected>Select a material</option>
                    <option value="${item['Material 1']}">${item['Material 1']}</option>
                    <option value="${item['Material 2']}">${item['Material 2']}</option>
                    <option value="${item['Material 3']}">${item['Material 3']}</option>
                `;
                materialCell.appendChild(materialSelect);

                const supplierCell = row.insertCell(2);
                const costPerUnitCell = row.insertCell(3);
                row.insertCell(4).textContent = '-'; // Placeholder for quantity
                row.insertCell(5).textContent = '-'; // Placeholder for total cost

                // Fetch supplier and cost per unit data for the selected material
                materialSelect.addEventListener('change', function() {
                    const selectedMaterial = materialSelect.value;
                    if (selectedMaterial) {
                        fetchSupplier(selectedMaterial, supplierCell,costPerUnitCell);
                    }
                });

                // Initial fetch for the default selected material
                //fetchSupplierAndCost(item['Material 1'], supplierCell);
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});

// Function to fetch supplier and cost per unit data for the selected material
function fetchSupplier(material, supplierCell, costPerUnitCell) {
    fetch(`http://127.0.0.1:5000/get_supplier_and_cost?material=${encodeURIComponent(material)}`)
        .then(response => response.json())
        .then(data => {
            console.log('Supplier and cost data received:', data);
            const supplierSelect = document.createElement('select');
            supplierSelect.innerHTML = `<option value="" disabled selected>Select a supplier</option>`;
            data.forEach(item => {
                console.info(item);
                supplierSelect.innerHTML += `<option value="${item['Supplier']}">${item['Supplier']}</option>`;
            })
            supplierCell.appendChild(supplierSelect);
            //supplierCell.textContent = data.supplier;
            //costPerUnitCell.textContent = data.cost_per_unit;
            // Event listener to set the cost per unit after the supplier has been selected
            supplierSelect.addEventListener('change', function() {
                const selectedSupplier = supplierSelect.value;
                const selectedData = data.find(item => item['Supplier'] === selectedSupplier);
                if (selectedData) {
                    costPerUnitCell.textContent = selectedData['Cost per unit'];
                }
            });
        })
            .catch(error => {
                console.error('Error fetching supplier and cost data:', error);
                supplierCell.textContent = 'Error';
                costPerUnitCell.textContent = 'Error';
         });
    }
