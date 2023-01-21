import { useState, useEffect } from "react"
import {
	MapPinIcon,
	AtSymbolIcon,
	PhoneIcon,
} from "@heroicons/react/24/outline"
import Image from "next/image"
import Link from "next/link"

const cluster_id = [
	"Data",
	"Other",
	"Online marketing",
	"Software",
	"Hardware",
	"Network",
	"IT",
]

const classBadge = [
	"bg-red-100 text-red-800",
	"bg-amber-100 text-amber-800",
	"bg-lime-100 text-lime-800",
	"bg-teal-100 text-teal-800",
	"bg-sky-100 text-sky-800",
	"bg-indigo-100 text-indigo-800",
	"bg-fuchsia-100 text-fuchsia-800",
]
export async function getServerSideProps(context) {
	return {
		props: { listCompanies: data },
	}
}

const AdviceCompany = ({ listCompanies }) => {
	console.log(listCompanies)
	const [listCompany, setListCompany] = useState([])

	useEffect(() => {
		async function getListCompany() {
			const amount = 12
			const url = `http://localhost:3000/api/randomcompany?amount=${amount}`
			const res = await fetch(url)
			const data = await res.json()
			setListCompany(data.listCompany)
		}
		getListCompany()
	}, [])

	return (
		<>
			<div className="flex-col flex items-center justify-center">
				<div className="w-3/4 flex items-center">
					<Image src="/advice.png" width={30} height={30} alt="advice logo" />
					<h1 className="text-2xl md:text-3xl font-semibold">
						สถานประกอบการน่าสนใจ
					</h1>
				</div>

				<div className="w-3/4 mt-3">
					{/* Card */}
					<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
						{listCompany.map((elem, index) => (
							<Link
								key={index}
								href={`/company/${elem["_id"]}`}
								target="_blank"
							>
								<div className="">
									<div
										className="bg-white shadow-md hover:shadow-lg hover:border-purple-400 rounded-md px-4 py-4 relative border border-gray-200"
										id="card"
									>
										<h1 className="text-lg">{elem.th_company_name}</h1>
										<div className="text-gray-500 text-sm mt-2" id="card-body">
											<p>
												<small className="flex items-start">
													<MapPinIcon className="mr-2" width={16} />
													{elem.province_base}
												</small>
											</p>

											<p>
												<small className="flex items-center">
													<AtSymbolIcon className="mr-2" width={16} />
													{elem.email}
												</small>
											</p>
											<p>
												<small className="flex items-center">
													<PhoneIcon className="mr-2" width={16} />
													{elem.phone_number}
												</small>
											</p>
										</div>

										<div id="card-footer" className="mt-5">
											<p className="mt-2">
												<span
													className={`${
														classBadge[elem.cluster]
													} text-xs font-medium mr-2 px-2.5 py-0.5 rounded `}
												>
													{cluster_id[elem.cluster]}
												</span>
											</p>
										</div>
									</div>
								</div>
							</Link>
						))}
					</div>
				</div>
			</div>
		</>
	)
}

export default AdviceCompany
