function getCookie(name) {
  	let matches = document.cookie.match(new RegExp(
    	"(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  	));
  	return matches ? decodeURIComponent(matches[1]) : undefined;
}

new Vue({
	el: '#payment-app',
	data: {
		options: true,
		driver: [],
		last_name: '',
		first_name: '',
		father_name: '',
		brand: '',
		model: '',
		car_year: '',
		insurance_amount: '',
		auto_class: '2',
		driver_year: '',
		experience: '',
		num_drivers: '',
		kbm: '1',
		dtp_third_person: '',
		dtp_ts_person: '',
		mechanic_damage: '',
		damage_third_person: '',
		grass: '',
		hijhacking: '',
		num_payments: '',
		insurance_term: '',
		kf_amount: '',
		anderight: '',
		insurance_amount_health: "100000",
		osago: '',
		insurance_sum: '',
		places: 'Все'
	},
	methods: {
		create_payment: function(){
			var csrftoken = getCookie('csrftoken');
			var data = JSON.stringify({
						"status":"Черновик",
						"first_name": this.first_name,
						"last_name": this.last_name,
						"father_name": this.father_name,
						"driver_age": parseInt(this.driver_year, 10),
						"experience": parseInt(this.experience, 10),
						"brand": this.brand,
						"model": this.model,
						"number_of_drivers": parseInt(this.num_drivers, 10),
						"kbm": parseFloat(this.kbm, 10),
						"car_year": parseInt(this.car_year, 10),
						"insurance_amount": parseFloat(this.insurance_amount, 10),
						"class_master": parseInt(this.auto_class, 10),
						"accident_caused_by_third_parties": this.dtp_third_person,
						"accident_caused_by_drivers_of_the_insured_car": this.dtp_ts_person,
						"damage": this.mechanic_damage,
						"broken_glass": this.grass,
						"unlawful_actions_of_third_parties": this.damage_third_person,
						"hijacking": this.hijhacking,
						"total_damage": true,
						"number_of_payments": parseInt(this.num_payments, 10),
						"insurance_period": parseInt(this.insurance_term, 10),
						"prize_kf": parseFloat(this.kf_amount, 10),
						"anderright_kf": parseFloat(this.anderight, 10),
						"insurance_liability": parseFloat(this.insurance_amount_health, 10),
						"insurance_prize_osago": parseFloat(this.osago, 10),
						"insurance_accident": parseFloat(this.insurance_sum, 10),
						"insurance_places": this.places,
						"admin":1});

			var config = {
  				method: 'post',
  				url: 'http://127.0.0.1:8000/policyholder/',
  				headers: { 
    				"X-CSRFToken": csrftoken, 
    				'Content-Type': 'application/json'
  				},
  				data : data
			};

			axios(config)
				.then(function (response) {
 					console.log(JSON.stringify(response.data));
				})
				.catch(function (error) {
  					console.log(error);
				});
		},
	}
})