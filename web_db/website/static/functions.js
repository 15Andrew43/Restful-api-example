function deleteUser(id) {
	console.log( 1543 );
	fetch("/users/" + id, {
		method: "DELETE",
		headers: {'Content-Type': 'application/json'},
		// body: JSON.stringify({ id: id }),
	})
	.then((_res) => {
		window.location.href = "/users";
	});
}

function addUser(nickname, email, rating) {
	console.log( 42 );
	fetch("/users", {
		method: "POST",
		headers: {'Content-Type': 'application/json'},
		body: JSON.stringify({ nickname: nickname, email: email , rating: rating}),
	})
	.then((_res) => {
		window.location.href = "/users";
	});
}

function modifying(id) {
	const cur_user = document.getElementById(id);
	var input = 
`<p id="modifying">
	<input type="text" name="m_nickname" placeholder="input nickname"/>
	<input type="email" name="m_email" placeholder="input email"/>
	<input type="number" name="m_rating" placeholder="input rating"/>
	<input type="button" value="modify" onClick="modifyUser(
															${id}, 
															document.getElementsByName('m_nickname')[0].value, 
															document.getElementsByName('m_email')[0].value, 
															document.getElementsByName('m_rating')[0].value)" /> 
</p>`;
	cur_user.insertAdjacentHTML('afterend', input);
}

function modifyUser(id, nickname, email, rating) {
	console.log( 179 );
	fetch("/users/" + id, {
		method: "PUT",
		headers: {'Content-Type': 'application/json'},
		body: JSON.stringify({ id: id, nickname: nickname, email: email , rating: rating}),
	})
	.then((_res) => {
		window.location.href = "/users";
	});
}