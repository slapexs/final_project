import { useState, useEffect } from "react"

const AdviceCompany = () => {
	const [users, setUser] = useState([])

	useEffect(() => {
		async function getUser() {
			const res = await fetch("https://jsonplaceholder.typicode.com/users")
			const data = await res.json()
			setUser(data)
		}

		getUser()
	}, [])

	return (
		<>
			<div className="sm:py-32 lg:py-24">
				<div className="flex-col flex items-center justify-center">
					<div className="w-3/4 flex items-center flex">
						<img src="./advice.png" className="w-12" />
						<h1 className="text-2xl">สถานประกอบการ น่าสนใจ</h1>
					</div>

					<div className="w-3/4 mt-3">
						{/* Card */}
						<div className="grid grid-cols-3 gap-4">
							{users.map((user) => (
								<div className="" key={user.id}>
									<div
										className="bg-white shadow-md rounded-md px-4 py-4 h-full relative"
										id="card"
									>
										<h1 className="text-2xl">{user.company.name}</h1>
										<div className="text-gray-500" id="card-body">
											<small>
												{user.address.street +
													" " +
													user.address.suite +
													" " +
													user.address.city +
													" " +
													user.address.zipcode}
											</small>

											<p>
												<small>{user.email}</small>
											</p>
											<p>
												<small>{user.phone}</small>
											</p>
										</div>

										<div id="card-footer" className="mt-5">
											<span class="bg-red-100 text-red-800 text-xs font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-red-900 dark:text-red-300">
												Online marketing
											</span>
										</div>
									</div>
								</div>
							))}
						</div>
					</div>
				</div>
			</div>
		</>
	)
}

export default AdviceCompany
