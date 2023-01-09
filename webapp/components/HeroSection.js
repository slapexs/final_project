import { useState } from "react"
import { MagnifyingGlassIcon } from "@heroicons/react/24/outline"

export default function Searchbox() {
	return (
		<>
			<div className="py-24 sm:py-32 lg:py-24">
				<div className="mx-auto max-w-7xl px-6 lg:px-6">
					<div className="text-center">
						<h1 className="text-4xl font-bold">ค้นหาสถานประกอบการ</h1>
						<p className="mt-2 text-gray-600">
							ระบุรายละเอียดความสนใจที่อยากฝึกงาน
						</p>
					</div>

					<div className="mt-4 justify-center flex gap-x-4">
						<input
							className="block w-2/4 py-2 px-3 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
							type="text"
							name="search"
							id="search"
							autoComplete="off"
							placeholder="สนใจฝึกงานด้านไหน?"
						/>

						<button className="px-4 py-2 inline-block bg-orange-400 rounded-lg text-white hover:bg-orange-500">
							ค้นหา <MagnifyingGlassIcon className="w-5 inline" />
						</button>
					</div>
				</div>
			</div>
		</>
	)
}
