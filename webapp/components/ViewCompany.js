import Image from "next/image"
import { useState, useEffect } from "react"

const ViewCompany = ({ ...props }) => {
	const [user, setUser] = useState([])

	const GetUser = async () => {
		const res = await fetch("https://jsonplaceholder.typicode.com/users")
		const data = await res.json()

		setUser(data)
	}
	useEffect(() => {
		GetUser()
	}, [])

	console.log(props.users)
	return (
		<>
			<div className="py-24 sm:py-30 flex justify-center">
				<div className="w-3/4">
					<div className="flex items-center">
						<Image src="/advice.png" width="48" height="48" alt="advice" />
						<h1 className="font-bold text-3xl text-gray-600">
							หมวดหมู่: <span className="capitalize">{props.name}</span>
						</h1>
					</div>

					<div className="mt-4">
						<ul>
							<div className="grid grid-cols-2 gap-4">
								{user.map((elem, index) => (
									<li
										key={index}
										className="border border-gray-300 p-2 rounded shadow-sm flex justify-between hover:shadow-lg"
									>
										<span>{elem.company.name}</span>
										<small className="text-gray-400">{elem.address.city}</small>
									</li>
								))}
							</div>
						</ul>
					</div>
				</div>
			</div>
		</>
	)
}

export default ViewCompany
