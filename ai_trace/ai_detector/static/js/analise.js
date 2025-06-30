document.addEventListener('DOMContentLoaded', function() {
  const dataTag = document.getElementById('percentuais-data');
  if (dataTag) {
    const percentuais = JSON.parse(dataTag.textContent);
    percentuais.forEach(function(val, idx) {
      const circle = document.querySelectorAll('.circle')[idx];
      const legenda = document.getElementById('legenda-' + idx);
      setTimeout(function() {
        if(circle && legenda) {
          circle.setAttribute('stroke-dasharray', val + ', 100');
          legenda.innerText = val + '%';
        }
      }, 300 + idx * 200);
    });
  }
});