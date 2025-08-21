document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.querySelector('.form');
    const cityInput = document.getElementById('city_input');
    
    searchForm.addEventListener('submit', handleSearch);
    
    cityInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            handleSearch(e);
        }
    });
    
    function handleSearch(event) {
        event.preventDefault();
        const cityName = cityInput.value.trim();
        
        if (cityName) {
            const cleanCityName = cityName.replace(/[^a-zA-Zа-яА-ЯёЁ\s-]/g, '');
            window.location.href = `/weather/${encodeURIComponent(cleanCityName)}`;
        }
    }
});