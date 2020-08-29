function addForm(type) {
    const formsets = document.getElementsByClassName('form');
    const maxForm = document.getElementById(`id_${type}_set-MAX_NUM_FORMS`).value;
    if (formsets.length < maxForm) {
        const counter = document.getElementById(`id_${type}_set-TOTAL_FORMS`);
        const cant = parseInt(counter.value) + 1;
        counter.value = cant;
        const hiddenForm = document.getElementsByClassName('hidden')[0];
        const clone = hiddenForm.cloneNode(true);
        clone.setAttribute('class', 'form');
        Array.from(clone.querySelectorAll('input, select')).forEach((element) => {
            element.setAttribute('id', element.getAttribute('id').replace(/__prefix__/g, cant));
            element.setAttribute('name', element.getAttribute('name').replace(/__prefix__/g, cant));
        });
        Array.from(clone.getElementsByTagName('label')).forEach((label) => {
            label.setAttribute('for', label.getAttribute('for').replace(/__prefix__/g, cant));
        })
        const container = document.getElementById('container');
        container.appendChild(clone);
        if (cant == maxForm)
            document.getElementById('btnAddForm').disabled = true;
    } else {
        console.log('Se excedió');
    }
}