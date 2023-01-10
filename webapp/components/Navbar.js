import { Fragment } from "react"
import { Disclosure, Menu, Transition } from "@headlessui/react"
import {
	Bars3Icon,
	XMarkIcon,
	ChevronDownIcon,
} from "@heroicons/react/24/outline"

const navigation = [
	{
		name: "สถานประกอบการทั้งหมด",
		href: "#",
		current: false,
	},
]

const cocmpany_category = [
	{ name: "Data", href: "#", current: false },
	{ name: "Hardware", href: "#", current: false },
	{ name: "IT", href: "#", current: false },
	{ name: "Network", href: "#", current: false },
	{ name: "Online marketing", href: "#", current: false },
	{ name: "Other", href: "#", current: false },
	{ name: "Software", href: "#", current: false },
]

function classNames(...classes) {
	return classes.filter(Boolean).join(" ")
}

export default function Navbar() {
	return (
		<Disclosure as="nav" className="bg-slate-200">
			{({ open }) => (
				<>
					<div className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
						<div className="relative flex h-16 items-center justify-between">
							<div className="absolute inset-y-0 left-0 flex items-center sm:hidden">
								{/* Mobile menu button*/}
								<Disclosure.Button className="inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
									<span className="sr-only">Open main menu</span>
									{open ? (
										<XMarkIcon className="block h-6 w-6" aria-hidden="true" />
									) : (
										<Bars3Icon className="block h-6 w-6" aria-hidden="true" />
									)}
								</Disclosure.Button>
							</div>
							<div className="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
								<div className="flex flex-shrink-0 items-center">
									<img
										className="block h-8 w-auto lg:hidden"
										src="./houseparty.png"
										alt="Intern assistant"
									/>
									<img
										className="hidden h-8 w-auto lg:block"
										src="./houseparty.png"
										alt="Intern assistant"
									/>
									<strong className="font-bold">Intern assistant</strong>
								</div>
								<div className="hidden sm:ml-6 sm:block">
									<div className="flex space-x-4  absolute right-0">
										{navigation.map((item) => (
											<a
												key={item.name}
												href={item.href}
												className={classNames(
													item.current
														? "bg-amber-600 text-white"
														: "text-gray-500 hover:bg-amber-500 hover:text-white",
													"px-3 py-2 rounded-md text-sm font-medium"
												)}
												aria-current={item.current ? "page" : undefined}
											>
												{item.name}
											</a>
										))}

										{/* Company category */}
										<Menu as="div" className="relative inline-block text-left">
											<div>
												<Menu.Button className="inline-flex w-full justify-center  px-4 py-2 text-sm font-medium text-gray-500 hover:bg-amber-500  hover:text-white rounded-md focus:ring-offset-gray-100">
													หมวดหมู่สถานประกอบการ
													<ChevronDownIcon
														className="-mr-1 ml-2 h-5 w-5"
														aria-hidden="true"
													/>
												</Menu.Button>
											</div>

											<Transition
												as={Fragment}
												enter="transition ease-out duration-100"
												enterFrom="transform opacity-0 scale-95"
												enterTo="transform opacity-100 scale-100"
												leave="transition ease-in duration-75"
												leaveFrom="transform opacity-100 scale-100"
												leaveTo="transform opacity-0 scale-95"
											>
												<Menu.Items className="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
													<div className="py-1">
														{cocmpany_category.map((elem, index) => (
															<Menu.Item key={index}>
																{({ active }) => (
																	<a
																		href={elem.href}
																		className={classNames(
																			elem.current
																				? "bg-gray-100 text-gray-900"
																				: "text-gray-700",
																			"block px-4 py-2 text-sm hover:bg-amber-200"
																		)}
																	>
																		{elem.name}
																	</a>
																)}
															</Menu.Item>
														))}
													</div>
												</Menu.Items>
											</Transition>
										</Menu>
									</div>
								</div>
							</div>
						</div>
					</div>

					{/* Dropdown sm */}
					<Disclosure.Panel className="sm:hidden">
						<div className="space-y-1 px-2 pt-2 pb-3">
							{navigation.map((item) => (
								<Disclosure.Button
									key={item.name}
									as="a"
									href={item.href}
									className={classNames(
										item.current
											? "bg-amber-600 text-white"
											: "text-gray-500 hover:bg-amber-500 hover:text-white",
										"block px-3 py-2 rounded-md text-base font-medium"
									)}
									aria-current={item.current ? "page" : undefined}
								>
									{item.name}
								</Disclosure.Button>
							))}
						</div>

						<div className="space-y-1 px-2 pt-2 pb-3">
							{/* Company category */}
							<Menu as="div" className="relative inline-block text-left">
								<div>
									<Menu.Button className="inline-flex w-full justify-center  px-4 py-2 text-base font-medium text-gray-500 hover:bg-amber-500  hover:text-white rounded-md focus:ring-offset-gray-100">
										หมวดหมู่สถานประกอบการ
										<ChevronDownIcon
											className="-mr-1 ml-2 h-5 w-5"
											aria-hidden="true"
										/>
									</Menu.Button>
								</div>

								<Transition
									as={Fragment}
									enter="transition ease-out duration-100"
									enterFrom="transform opacity-0 scale-95"
									enterTo="transform opacity-100 scale-100"
									leave="transition ease-in duration-75"
									leaveFrom="transform opacity-100 scale-100"
									leaveTo="transform opacity-0 scale-95"
								>
									<Menu.Items className="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
										<div className="py-1">
											{cocmpany_category.map((elem, index) => (
												<Menu.Item key={index}>
													{({ active }) => (
														<a
															href={elem.href}
															className={classNames(
																elem.current
																	? "bg-gray-100 text-gray-900"
																	: "text-gray-700",
																"block px-4 py-2 text-sm hover:bg-amber-200"
															)}
														>
															{elem.name}
														</a>
													)}
												</Menu.Item>
											))}
										</div>
									</Menu.Items>
								</Transition>
							</Menu>
						</div>
					</Disclosure.Panel>
				</>
			)}
		</Disclosure>
	)
}
