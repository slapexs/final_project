import Image from "next/image"
import { MapPinIcon } from "@heroicons/react/24/outline"
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

function concatClass(...classes) {
	return classes.filter(Boolean).join(" ")
}

export default function ResultCompany({ cluster, companies }) {
	return (
		<>
			<div className="w-full">
				<div className="justify-center flex">
					<div className="w-3/4 flex items-center">
						<Image src="/advice.png" alt="advice icon" width="48" height="48" />
						<h1 className="text-2xl">หมวดหมู่: {cluster_id[cluster]}</h1>
					</div>
				</div>

				<div className="flex justify-center mt-2">
					<div className="w-3/4">
						<ul>
							<div className="grid grid-cols-2 gap-4">
								{companies.map((elem, index) => (
									<Link href={`/company/${elem["_id"]}`} key={index}>
										<li className="border border-gray-300 p-2 shadow-sm flex justify-between hover:shadow-lg rounded">
											<div>
												<h1>{elem.th_company_name}</h1>
												<p className="text-orange-400 text-xs">
													{elem.short_company}
												</p>
											</div>
											<small className="text-gray-400 flex items-center">
												<MapPinIcon className="w-3 inline mr-1" />{" "}
												{elem.province_base}
											</small>
										</li>
									</Link>
								))}
							</div>
						</ul>
					</div>
				</div>
			</div>
		</>
	)
}
