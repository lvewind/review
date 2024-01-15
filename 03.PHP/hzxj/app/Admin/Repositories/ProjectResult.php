<?php

namespace App\Admin\Repositories;

use App\Models\ProjectResult as Model;
use Dcat\Admin\Repositories\EloquentRepository;

class ProjectResult extends EloquentRepository
{
    /**
     * Model.
     *
     * @var string
     */
    protected $eloquentClass = Model::class;
}
