import { useState } from "react"
import { MagnifyingGlassIcon, ArrowPathIcon } from "@heroicons/react/24/outline"

import ResultCompany from "./ResultCompany"
import AdviceCompany from "./AdviceCompany"

export default function Searchbox() {
	const [searchKeyword, setSearchKeyword] = useState("")
	const [searching, setSearching] = useState(false)
	const [resultClusterId, setResultClusterId] = useState(null)
	const [resultCompany, setResultCompany] = useState([])

	function handleKeyword(e) {
		setSearchKeyword(e.target.value)
	}

	async function getCompanyWithCluster(cluster_id) {
		const api_url = `http://localhost:3000/api/getcompany?cluster=${cluster_id}`
		const res = await fetch(api_url)
		const data = await res.json()
		setResultCompany(data.data)
	}

	async function analyzeCluster() {
		const url = "http://13.229.79.190/search"
		setSearching(true)
		const res = await fetch(url, {
			method: "POST",
			body: JSON.stringify({ keyword: searchKeyword }),
			headers: {
				"Content-Type": "application/json",
			},
		})

		const data = await res.json()
		setSearching(false)
		setResultClusterId(data.cluster)
		// Get all companies in cluster
		getCompanyWithCluster(data.cluster)
		document.querySelector("#search").value = ""
	}

	return (
		<>
			<div className="py-24 sm:py-32 lg:py-24">
				<div className="mx-auto max-w-7xl px-6 lg:px-6">
					<div className="text-center">
						<h1 className="text-5xl font-bold">ค้นหาสถานประกอบการ</h1>
						<p className="mt-2 text-gray-600">
							ระบุรายละเอียดความสนใจที่อยากฝึกงาน
						</p>
					</div>

					<div className="mt-10 flex gap-x-4 items-end justify-center">
						<textarea
							name="search"
							id="search"
							className="block w-2/4 py-2 px-3 rounded-md bg-slate-50 border border-gray-400 border-1 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm disabled:bg-zinc-200"
							placeholder="สนใจฝึกงานด้านไหน?"
							onChange={handleKeyword}
							disabled={searching}
						/>

						<button
							className={
								searching
									? "px-4 py-2 inline-block rounded-lg text-white bg-amber-400 "
									: "px-4 py-2 inline-block rounded-lg text-white bg-amber-500 hover:bg-amber-600"
							}
							onClick={analyzeCluster}
							disabled={searching}
						>
							{searching ? (
								<ArrowPathIcon className="w-5 inline animate-spin" />
							) : (
								<MagnifyingGlassIcon className="w-5 inline" />
							)}

							{searching ? "กำลังค้นหา" : "ค้นหา"}
						</button>
					</div>
				</div>
			</div>

			{/* Result search company */}
			{resultClusterId ? (
				<ResultCompany cluster={resultClusterId} companies={resultCompany} />
			) : (
				<AdviceCompany />
			)}
		</>
	)
}
