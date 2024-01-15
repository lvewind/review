<?php

namespace App\Admin\Repositories;

use App\Models\InspectionResult as Model;
use Dcat\Admin\Repositories\EloquentRepository;

class InspectionResult extends EloquentRepository
{
    /**
     * Model.
     *
     * @var string
     */
    protected $eloquentClass = Model::class;
}
