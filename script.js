document.getElementById('loadData').addEventListener('click', function() {
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
                    <option value="${item['Material 1']}">${item['Material 1']}</option>
                    <option value="${item['Material 2']}">${item['Material 2']}</option>
                    <option value="${item['Material 3']}">${item['Material 3']}</option>
                `;
                materialCell.appendChild(materialSelect);

                row.insertCell(2).textContent = '-'; // Placeholder for supplier
                row.insertCell(3).textContent = '-'; // Placeholder for cost per unit
                row.insertCell(4).textContent = '-'; // Placeholder for quantity
                row.insertCell(5).textContent = '-'; // Placeholder for total cost
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});