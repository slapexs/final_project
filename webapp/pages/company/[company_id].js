import { useRouter } from "next/router"
import { useState, useEffect } from "react"
import {
	MapPinIcon,
	AtSymbolIcon,
	PhoneIcon,
	HomeIcon,
	GlobeAltIcon,
	UserIcon,
	CodeBracketIcon,
} from "@heroicons/react/24/outline"

import Head from "next/head"

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
	const { company_id } = context.query
	const url = `http://localhost:3000/api/getcompanyby_id?company_id=${company_id}`
	const res = await fetch(url)
	const data = await res.json()

	return {
		props: { company: data.data[0] },
	}
}

const CompanyByID = ({ company }) => {
	const router = useRouter()
	const { company_id } = router.query

	return (
		<>
			<Head>
				<title>ข้อมูลบริษัท | {company.th_company_name}</title>
				<meta
					name="description"
					content="ระบบแนะนำบริษัทสำหรับฝึกงานตามความสนวจ ด้วยเทตโนโลยีปัญญาประดิษฐ์ | Recommended System of Internship's Company"
				/>
				<meta name="viewport" content="width=device-width, initial-scale=1" />
				<link rel="icon" href="/houseparty.png" />
			</Head>

			<div className="py-24 sm:py-32 lg:py-24 flex justify-center">
				{/* Content */}
				<div className="w-3/4">
					<h1 className="text-3xl font-bold">{company.th_company_name}</h1>
					<p className="text-gray-400">
						{company.eng_company_name} ({company.short_company})
					</p>

					<p className="mt-2">
						<span
							className={`${
								classBadge[company.cluster]
							} text-xs font-medium mr-2 px-2.5 py-0.5 rounded `}
						>
							{cluster_id[company.cluster]}
						</span>
					</p>

					{/* Grid col 2 columns */}
					<div className="grid grid-cols-2 gap-4 mt-10">
						{/* Company detail */}
						<div className="">
							<p className="font-light text-gray-400">ข้อมูลบริษัท</p>
							<div className="mt-2">
								<p className="mb-1 flex gap-x-3">
									<UserIcon width={20} className="" /> {company.owner}
								</p>
								<p className="mb-1 flex gap-x-3">
									<CodeBracketIcon width={20} className="" />{" "}
									{company.type_business}
								</p>
								<p className="mb-1 flex gap-x-3">
									<HomeIcon width={20} className="" /> {company.province_base}
								</p>
							</div>
						</div>

						<div className="">
							<p className="font-light text-gray-400">ข้อมูลติดต่อ</p>
							<div className="mt-2">
								<p className="mb-1 flex gap-x-3">
									<MapPinIcon width={20} className="" /> {company.address}
								</p>
								<p className="mb-1 flex gap-x-3">
									<AtSymbolIcon width={20} className="" /> {company.email}
								</p>
								<p className="mb-1 flex gap-x-3">
									<PhoneIcon width={20} className="" /> {company.phone_number}
								</p>
								<p className="mb-1 flex gap-x-3">
									<GlobeAltIcon width={20} className="" /> {company.website}
								</p>
							</div>
						</div>
					</div>

					{/* Detail */}
					<div className="mt-10">
						<p className="font-light text-gray-400">รายละเอียดธุรกิจ</p>
						<div className="mt-2">
							<p className="mb-1 flex gap-x-3">{company.detail}</p>
						</div>
					</div>
				</div>
			</div>
		</>
	)
}

export default CompanyByID
