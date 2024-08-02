document.addEventListener("DOMContentLoaded", () => {
	handleLoginForm();
	handleTokenAndLoginLink();
	handlePlaceDetails();
  });

  // Manejo del formulario de login
  function handleLoginForm() {
	const loginForm = document.getElementById("login-form");

	if (loginForm) {
	  loginForm.addEventListener("submit", async (event) => {
		event.preventDefault();

		const email = document.getElementById("email").value;
		const password = document.getElementById("password").value;

		try {
		  const response = await fetch("http://127.0.0.1:5000/login", {
			method: "POST",
			headers: {
			  "Content-Type": "application/json",
			},
			body: JSON.stringify({ email, password }),
		  });

		  if (response.ok) {
			const data = await response.json();
			document.cookie = `token=${data.access_token}; path=/;`;
			window.location.href = "index.html";
		  } else {
			const errorData = await response.json();
			alert(`Login failed: ${errorData.description}`);
		  }
		} catch (error) {
		  console.error("Error:", error);
		  alert("An error occurred. Please try again.");
		}
	  });
	}
  }

  // Verificar token y manejar visibilidad del enlace de login
  function handleTokenAndLoginLink() {
	const token = getCookie("token");
	const loginLink = document.getElementById("login-link");

	if (!token) {
	  if (loginLink) {
		loginLink.style.display = "block";
	  }
	} else {
	  if (loginLink) {
		loginLink.style.display = "none";
	  }
	  fetchPlaces(token);
	}
  }

  // Obtener valor de una cookie
  function getCookie(name) {
	const value = `; ${document.cookie}`;
	const parts = value.split(`; ${name}=`);
	if (parts.length === 2) return parts.pop().split(";").shift();
  }

  // Obtener lista de lugares desde el servidor
  async function fetchPlaces(token) {
	try {
	  const response = await fetch("http://127.0.0.1:5000/places", {
		headers: {
		  Authorization: `Bearer ${token}`,
		},
	  });

	  if (response.ok) {
		const places = await response.json();
		displayPlaces(places);
	  } else {
		console.error("Failed to fetch places:", response.statusText);
		document.getElementById("login-link").style.display = "block";
	  }
	} catch (error) {
	  console.error("Error:", error);
	  document.getElementById("login-link").style.display = "block";
	}
  }

  // Mostrar la lista de lugares en el DOM
  function displayPlaces(places) {
	const placesList = document.getElementById("places-list");
	placesList.innerHTML = "";

	places.forEach((place) => {
	  const placeElement = document.createElement("div");
	  placeElement.innerHTML = `
		  <div class="place-card">
			<div class="place-image">
			  <img src="${place.img_url}" alt="${place.name}">
			  <h2>${place.name}</h2>
			  <p>Price per night: <span>$${place.price_per_night}</span></p>
			  <p>Location: <span>${place.location}</span></p>
			  <div class="details-button">
				<a href="place.html?placeId=${place.id}">
				  <button>View Details</button>
				</a>
			  </div>
			</div>
		  </div>
		`;
	  placesList.appendChild(placeElement);
	});
  }

  // Manejo de detalles de lugares
  function handlePlaceDetails() {
	const token = getCookie("token");
	const placeId = getPlaceIdFromURL();

	if (token && placeId) {
	  fetchPlaceDetails(token, placeId)
		.then((isValid) => {
		  if (isValid) {
			document.getElementById("add-review").style.display = "block";
		  } else {
			document.getElementById("add-review").style.display = "none";
		  }
		})
		.catch((error) => {
		  console.error("Error:", error);
		  document.getElementById("add-review").style.display = "none";
		});
	} else {
	  document.getElementById("add-review").style.display = "none";
	}
  }

  // Obtener el ID del lugar desde la URL
  function getPlaceIdFromURL() {
	const params = new URLSearchParams(window.location.search);
	const placeId = params.get("placeId");
	console.log("Place ID from URL:", placeId); // Añadir un log para verificar el placeId
	return placeId;
  }

  // Obtener detalles del lugar desde el servidor
  async function fetchPlaceDetails(token, placeId) {
	try {
	  const response = await fetch(`http://127.0.0.1:5000/places/${placeId}`, {
		headers: {
		  Authorization: `Bearer ${token}`,
		},
	  });

	  if (response.ok) {
		const place = await response.json();
		displayPlaceDetails(place);
		return true;
	  } else {
		console.error("Failed to fetch place details:", response.statusText);
		return false;
	  }
	} catch (error) {
	  console.error("Error:", error);
	  return false;
	}
  }

  // Mostrar los detalles del lugar en el DOM
  function displayPlaceDetails(place) {
	const placeDetails = document.getElementById("place-details");
	placeDetails.innerHTML = `
		  <section id="place-details">
		  			<h1>${place.name}</h1>
					  <div class="place-details">
					  	<div class="place-info">
						  <img src="${place.img_url}" alt="${place.name}">
							<p>Host: <span>${place.max_guests}</span></p>
							<p>Price: <span>${place.price_per_night}</span></p>
							<p>Locations: <span>${place.location}</span></p>
							<p>Amenities: <span>${place.amenity}</span></p>
							<p>Description: <span>${place.description}</span></p>
						</div>
					  </div>
					  <h2>Reviews</h2>
					  <div class="place-image-large"></div>
					  <div class="place-info"></div>
				  </section>
			  `;
  }

  document.addEventListener("DOMContentLoaded", () => {
	handleLoginForm();
	handleTokenAndLoginLink();
	handlePlaceDetails();

	const reviewForm = document.getElementById("review-form");
	const token = getCookie("token");
	const placeId = getPlaceIdFromURL();

	if (reviewForm && token) {
	  reviewForm.addEventListener("submit", async (event) => {
		event.preventDefault();
		const reviewText = document.getElementById("review-text").value;
		const reviewStars = document.getElementById("review-stars").value;
		await submitReview(token, placeId, reviewStars, reviewText);
		await fetchReviews(token, placeId); // Fetch and display reviews after submitting a new review
	  });
	} else if (reviewForm) {
	  window.location.href = "index.html";
	}
  });

  async function submitReview(token, placeId, rating, comment) {
	try {
	  const response = await fetch(
		`http://127.0.0.1:5000/places/${placeId}/reviews`,
		{
		  method: "POST",
		  headers: {
			"Content-Type": "application/json",
			Authorization: `Bearer ${token}`,
		  },
		  body: JSON.stringify({ rating, comment }),
		}
	  );

	  if (response.ok) {
		alert("Review submitted successfully!");
		document.getElementById("review-text").value = "";
		document.getElementById("review-stars").value = "5"; // Reset rating to default
	  } else {
		const errorData = await response.json();
		alert(`Failed to submit review: ${errorData.description}`);
	  }
	} catch (error) {
	  console.error("Error:", error);
	  alert("An error occurred. Please try again.");
	}
  }

  async function fetchReviews(token, placeId) {
	try {
	  const response = await fetch(
		`http://127.0.0.1:5000/places/${placeId}/reviews`,
		{
		  headers: {
			Authorization: `Bearer ${token}`,
		  },
		}
	  );

	  if (response.ok) {
		const reviews = await response.json();
		displayReviews(reviews);
	  } else {
		console.error("Failed to fetch reviews:", response.statusText);
	  }
	} catch (error) {
	  console.error("Error:", error);
	}
  }

  function displayReviews(reviews) {
	const reviewsContainer = document.getElementById("reviews");
	reviewsContainer.innerHTML = "";

	reviews.forEach((review) => {
	  const reviewElement = document.createElement("div");
	  reviewElement.classList.add("review");
	  reviewElement.innerHTML = `
	  <div class="review-card">
			  <p><strong>Comment:</strong> ${review.comment}</p>
		  <p><strong>Rating:</strong> <span>${"★".repeat(review.rating)}${"☆".repeat(
		5 - review.rating
	  )}</span></p>
	  </div>
		`;
	  reviewsContainer.appendChild(reviewElement);
	});
  }

  // Función para obtener el valor de una cookie
  function getCookie(name) {
	const value = `; ${document.cookie}`;
	const parts = value.split(`; ${name}=`);
	if (parts.length === 2) return parts.pop().split(";").shift();
  }

  // Función para obtener el ID del lugar desde la URL
  function getPlaceIdFromURL() {
	const params = new URLSearchParams(window.location.search);
	const placeId = params.get("placeId");
	return placeId;
  }

  // Manejo de detalles de lugares
  function handlePlaceDetails() {
	const token = getCookie("token");
	const placeId = getPlaceIdFromURL();

	if (token && placeId) {
	  fetchPlaceDetails(token, placeId)
		.then((isValid) => {
		  if (isValid) {
			document.getElementById("add-review").style.display = "block";
			fetchReviews(token, placeId); // Fetch and display reviews when loading place details
		  } else {
			document.getElementById("add-review").style.display = "none";
		  }
		})
		.catch((error) => {
		  console.error("Error:", error);
		  document.getElementById("add-review").style.display = "none";
		});
	} else {
	  document.getElementById("add-review").style.display = "none";
	}
  }
